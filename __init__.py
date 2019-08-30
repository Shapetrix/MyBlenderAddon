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

from . test_op    import Test_OT_Operator
# Test_OT_Operator()

from . test_panel import Test_PT_Panel
# Test_PT_Panel()

classes = (Test_OT_Operator, Test_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
# def register():
#     Test_OT_Operator.register()
#     Test_PT_Panel.register()
#     print("Registered My Addon")
#
# def unregister():
#     Test_OT_Operator.register()
#     Test_PT_Panel.register()
#     print("Unregistered My Addon")
