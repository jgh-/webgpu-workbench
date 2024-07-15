include(FetchContent)

FetchContent_Declare(DAWN_EXT 
    GIT_REPOSITORY "https://dawn.googlesource.com/dawn"
    GIT_TAG "main"
    GIT_SUBMODULES ""
    DOWNLOAD_NO_EXTRACT 1
    CONFIGURE_COMMAND "python3 tools/fetch_dawn_dependencies.py"
    INSTALL_DIR "${PROJECT_SOURCE_DIR}/third_party"
    CMAKE_ARGS
        "-DDAWN_ENABLE_INSTALL=ON -DDAWN_BUILD_MONOLITHIC_LIBRARY=ON -DCMAKE_BUILD_TYPE=Debug -DBUILD_SAMPLES=OFF"
    
    OVERRIDE_FIND_PACKAGE
)

FetchContent_MakeAvailable(DAWN_EXT)