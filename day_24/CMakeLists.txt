configure_file(pieces.txt pieces.txt COPYONLY)

add_executable(day_24 day_24.cpp)
target_link_libraries(day_24)