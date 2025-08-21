if hou.isUIAvailable():
    import hdefereval
    from hutil.Qt import QtCore, QtWidgets

    def _ask():
        msg = QtWidgets.QMessageBox()
        msg.setText("Turn on autosave?")
        msg.setInformativeText("Automatic YES in 5 seconds...")
        msg.setStandardButtons(QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        msg.setDefaultButton(QtWidgets.QMessageBox.No)

        timer = QtCore.QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: (msg.done(QtWidgets.QMessageBox.Yes)))
        timer.start(5000)

        result = msg.exec_()
        timer.stop()

        if result == QtWidgets.QMessageBox.Yes:
            hou.hscript("autosave on")
        else:
            hou.hscript("autosave off")

    hdefereval.execute_deferred(_ask)