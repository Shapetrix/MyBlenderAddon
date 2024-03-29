bl_info = {
    "name": "Move X Axis",
    "category": "Object",
}

import bpy

class ObjectMoveX(bpy.types.Operator):
    """My Object Move X Script"""      #Use this as a tooltip for menu items and buttons
    bl_idname = "object.move_x"        #Unique identifier for buttons and menu items to reference
    bl_label = "Move X by One"         #Display name in the interface
    bl_options = {'REGISTER', 'UNDO'}  #Enable undo for the operator

    def execute(self, context):        #execute() is called when running the operator

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return {'FINISHED'}           #Lets Blender know the operator finished successfully

def register():
    bpy.utils.register_class(ObjectMoveX)

def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

#This allows you to run the script directly from blender's Text editor
#to test the add-on without having to install it
if __name__ == "__main__":
    register()
