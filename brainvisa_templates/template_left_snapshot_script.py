#import anaSulciSnapshot

#res = anaSulciSnapshot.main( ['-g', u'BVDIR/subjects/SUBJECT/t1mri/default_acquisition/default_analysis/folds/3.1/default_session_auto/LSUBJECT_default_session_auto.arg',
#'--label-mode', 'label', '-m', u'BVDIR/subjects/SUBJECT/t1mri/default_acquisition/default_analysis/segmentation/mesh/SUBJECT_Lwhite.gii',
#'--orientation', 'left', '-o', '/tmp/bv_60710_24.jpg', '--hie', '/Applications/brainvisa/share/brainvisa-share-4.4/nomenclature/hierarchy/sulcal_root_colors.hie',
#'--translation', '/Applications/brainvisa/share/brainvisa-share-4.4/nomenclature/translation/sulci_model_2008.trl',
#'--size', '10000,10000',
#'-t', u'BVDIR/subjects/SUBJECT/t1mri/default_acquisition/registration/RawT1-SUBJECT_default_acquisition_TO_Talairach-ACPC.trm'] )

import imp
anasul = imp.find_module( "anaSulciSnapshot", [ "BVHOME/bin/real-bin" ] )
anaSulciSnapshot = imp.load_module( "anaSulciSnapshot", anasul[0], anasul[1], anasul[2] )
anasul[0].close()



import os, sys, sip, numpy, time
from optparse import OptionParser
import sigraph
from soma import aims, aimsalgo
import anatomist.direct.api as anatomist
import PyQt4.QtCore as qt
import PyQt4.QtGui as qtgui

a = anatomist.Anatomist()
p = a.theProcessor()

def setCamera(win, orientation):
    q = aims.Quaternion()
    q2 = aims.Quaternion()
    if orientation == 'top' : # ok
        q.fromAxis([0, 0, 1], -numpy.pi/2)
    elif orientation == 'bottom' : # ok
        q.fromAxis([0, 0, 1], numpy.pi/2)
        q2.fromAxis([1, 0, 0], numpy.pi)
        q = q.compose(q2)
    elif orientation == 'left' : # ok
        q.fromAxis([0, 1, 0], numpy.pi / 2.)
        q2.fromAxis([1, 0, 0], numpy.pi / 2.)
        q = q.compose(q2)
    elif orientation == 'SIDE' : # ok
        q.fromAxis([0, 1, 0], -numpy.pi / 2.)
        q2.fromAxis([1, 0, 0], numpy.pi / 2.)
        q = q.compose(q2)
    elif orientation == 'back' : # ?
        q.fromAxis([1, 0, 0], -numpy.pi / 2)
        q2.fromAxis([0, 1, 0], numpy.pi)
        q = q.compose(q2)
    elif orientation == 'front' : # ?
        q.fromAxis([1, 0, 0], numpy.pi / 2)
    elif orientation.startswith('auto='):
        v = [float(x) for x in orientation.split('=')[1].split(',')]
        q.setVector(v)
    a.camera(windows=[win], zoom=1,
        observer_position=[10., 10., 10.],
        view_quaternion=q.vector(), force_redraw=True)


transfile='BVHOME/share/brainvisa-share-4.5/nomenclature/translation/sulci_model_2008.trl'
orientation='left'
trm_name='BVDIR/subjects/SUBJECT/t1mri/default_acquisition/registration/RawT1-SUBJECT_default_acquisition_TO_Talairach-ACPC.trm'
graphname='BVDIR/subjects/SUBJECT/t1mri/default_acquisition/default_analysis/folds/3.1/default_session_auto/LSUBJECT_default_session_auto.arg'
meshname='BVDIR/subjects/SUBJECT/t1mri/default_acquisition/default_analysis/segmentation/mesh/SUBJECT_Lwhite.gii'
imagename='SNAPDIR/left_lateral_SUBJECT.jpg'
selected_sulci=''
wingeom=[1000,1000]
label_state='label'
hiename='BVHOME/share/brainvisa-share-4.5/nomenclature/hierarchy/sulcal_root_colors.hie'

ag = a.loadObject(graphname)
g = ag.graph()
aobjects = [ag]

am = a.loadObject(meshname)
aobjects.append(am)


ahie = a.loadObject(hiename)

destination = a.centralRef
origin = a.createReferential()
t=a.loadTransformation(trm_name,origin,destination)

#motion = aims.GraphManip.talairach(ag.graph())
#vector = motion.toMatrix()[:3,3].tolist() + \
#motion.toMatrix()[:3,:3].T.ravel().tolist()
#t = a.execute("LoadTransformation",
#            **{'matrix' : vector,
#            'origin' : origin.getInternalRep(),
#            'destination' : destination.getInternalRep()})
#cdt = a.Transformation(a, t.trans())
ag.setReferential(origin.internalRep)

am.setReferential(origin.internalRep)

win = a.createWindow(wintype='3D', no_decoration=True,
        options= {'wflags' : int(qt.Qt.X11BypassWindowManagerHint | qt.Qt.WindowStaysOnTopHint) })

add_graph_nodes = True


a.addObjects(aobjects, win, add_graph_nodes=add_graph_nodes )

win.setHasCursor(0)
win.Refresh()
# hide toolbar/menu
win.showToolbox(0)

ag.setColorMode(ag.Normal)
ag.updateColors()
ag.notifyObservers()
ag.setChanged()

setCamera(win, orientation)
win.internalRep.focusView()
info = a.execute('ObjectInfo', objects=[win])
res = info.result()
info = [x for x in res][0]
bb = info['boundingbox_min'], info['boundingbox_max']
bb = list(bb[0]), list(bb[1])

desktop_geometry = qtgui.qApp.desktop().geometry()
desktop_geometry.setWidth( wingeom[0] )
desktop_geometry.setHeight( wingeom[1] )
win.setFocus()
win.raise_()

coords=desktop_geometry.getCoords()

a.execute("WindowConfig", windows=[win],
        geometry=coords, snapshot=imagename)
