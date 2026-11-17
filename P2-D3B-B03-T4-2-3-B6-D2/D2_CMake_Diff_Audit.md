# D2_CMake_Diff_Audit

## Scope
- Only authorized file: `app/DumpShortcuts/CMakeLists.txt`
- Before SHA256: `d4f8a2a3b098562cdbe9ecc5252729679bc133fed1d96a976349224189a0154a`
- After SHA256: `b7a28067953be6be09f3679b41ef144e0d991b4ce3579094deee70966628c67a`
- Added lines: 10; Removed lines: 0
- Added copy commands: 8 (D0-1 frozen list; no duplicates; 17 D1 commands retained)
- No changes to windeployqt, GenerateManual, PATH, or any other file.

## Added DLLs
- brotlicommon.dll
- zlib1.dll
- IlmThread-3_3.dll
- OpenEXRCore-3_3.dll
- deflate.dll
- libsharpyuv.dll
- lcms2-2.dll
- liblzma.dll

## Unified diff
```diff
--- D1_before
+++ D2_after
@@ -49,6 +49,16 @@
         COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/minizip.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
         COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/poly2tri.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
         COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/pugixml.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+
+        # Second- and third-level recursive dependencies of the DLLs above.
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/brotlicommon.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/zlib1.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/IlmThread-3_3.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/OpenEXRCore-3_3.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/deflate.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/libsharpyuv.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/lcms2-2.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
+        COMMAND ${CMAKE_COMMAND} -E copy_if_different "${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET}/bin/liblzma.dll" "$<TARGET_FILE_DIR:DumpShortcuts>"
     )
     
     # Run windeployqt which copies the Qt dlls into the deployable folder, along with necessary runtime dlls by the compiler
```
