# D1_CMake_Diff_Audit

## Scope
- Only authorized file: `app/DumpShortcuts/CMakeLists.txt`
- Before SHA256: `90a45d05529cdbe2581718a5d7bbcecf29dab1d62b7e6c254f07dd5c7957e61a`
- After SHA256: `d4f8a2a3b098562cdbe9ecc5252729679bc133fed1d96a976349224189a0154a`
- Added lines: 19; Removed lines: 0
- Added commands: 17 `cmake -E copy_if_different` lines inside the existing Windows POST_BUILD block.
- Existing direct-dependency copies and windeployqt invocation unchanged.

## Unified diff
```diff
--- before
+++ after
@@ -30,6 +30,25 @@
         COMMAND ${CMAKE_COMMAND} -E copy_if_different "$<TARGET_FILE:freetype>" "$<TARGET_FILE_DIR:DumpShortcuts>"
         COMMAND ${CMAKE_COMMAND} -E copy_if_different "$<TARGET_FILE:tinyxml2::tinyxml2>" "$<TARGET_FILE_DIR:DumpShortcuts>"
         COMMAND ${CMAKE_COMMAND} -E copy_if_different "$<TARGET_FILE:miniz::miniz>" "$<TARGET_FILE_DIR:DumpShortcuts>"
+
+        # Recursive third-party dependencies required by DumpShortcuts at runtime.
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/brotlidec.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/bz2.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/libpng16.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/Iex-3_3.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/Imath-3_2.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/OpenEXR-3_3.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/jpeg8.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/openjp2.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/raw.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/tiff.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/libwebp.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/libwebpdecoder.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/libwebpmux.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/kubazip.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/minizip.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/poly2tri.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/pugixml.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
     )
     
     # Run windeployqt which copies the Qt dlls into the deployable folder, along with necessary runtime dlls by the compiler
```
