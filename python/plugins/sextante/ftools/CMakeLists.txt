FILE(GLOB PY_FILES *.py)
FILE(GLOB OTHER_FILES copyright.txt)
FILE(GLOB ICON_FILES icons/*.png)

PLUGIN_INSTALL(sextante ./ftools ${PY_FILES} ${OTHER_FILES})
PLUGIN_INSTALL(sextante ./ftools/icons ${ICON_FILES})
