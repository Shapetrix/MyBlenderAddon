bl_info = {
    "name" : "My_addon",
    "author" : "brandon humfleet",
    "description" : "test addon",
    "blender" : (2, 80, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic",
}

import bpy

class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view3d.cursor_center', text="Center 3D cursor")
