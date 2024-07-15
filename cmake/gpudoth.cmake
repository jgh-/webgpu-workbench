include(FetchContent)

FetchContent_Declare(EXT_GPU_H 
    URL "https://raw.githubusercontent.com/AnswerDotAI/gpu.cpp/main/gpu.h"
    SOURCE_DIR "${PROJECT_SOURCE_DIR}/third_party/include/gpu"
    DOWNLOAD_DIR "${PROJECT_SOURCE_DIR}/third_party/include/gpu"
    DOWNLOAD_NO_EXTRACT 1
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    CONFIGURE_COMMAND ""
)

FetchContent_Declare(EXT_GPU_UTILS_LOGGING_H 
    URL "https://raw.githubusercontent.com/AnswerDotAI/gpu.cpp/main/utils/logging.h"
    SOURCE_DIR "${PROJECT_SOURCE_DIR}/third_party/include/gpu/utils"
    DOWNLOAD_DIR "${PROJECT_SOURCE_DIR}/third_party/include/gpu/utils"
    DOWNLOAD_NO_EXTRACT 1
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    CONFIGURE_COMMAND ""
)

FetchContent_MakeAvailable(EXT_GPU_H)
FetchContent_MakeAvailable(EXT_GPU_UTILS_LOGGING_H)

add_library(GpuDotH INTERFACE)
add_dependencies(GpuDotH EXT_GPU_H EXT_GPU_UTILS_LOGGING_H)
target_include_directories(GpuDotH SYSTEM INTERFACE "${PROJECT_SOURCE_DIR}/third_party/include")
