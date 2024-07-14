set(TARGET_NAME webgpu_init)

add_executable(${TARGET_NAME} ${TARGET_NAME}.cpp)
target_link_libraries(${TARGET_NAME} dawn::webgpu_dawn dawn::dawn_public_config)
target_include_directories(${TARGET_NAME} INTERFACE $<TARGET_PROPERTY:dawn_public_config,INTERFACE_INCLUDE_DIRECTORIES>)
add_custom_command(TARGET ${TARGET_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${PROJECT_SOURCE_DIR}/third_party/bin"
        $<TARGET_FILE_DIR:${TARGET_NAME}>)