bl_info = {
    "name": "Labyrinth",
    "category": "Import-Export",
}

import bpy

def write_generic_game_scenes(filePath):
    print("WRITING FILE!"+filePath)

class GenericGameScenesExport(bpy.types.Operator):
    """Export Generic Game Scenes"""
    bl_idname = "object.export_generic_game_scenes"
    bl_label = "Generic Game Scene (.toml)"
    bl_options = {'REGISTER'}
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
    filename = bpy.props.StringProperty()
    directory = bpy.props.StringProperty(subtype="FILE_PATH")
    def execute(self, context):
        write_generic_game_scenes(self.filepath)
        return {'FINISHED'}
    def invoke(self, context, event):
        self.filename = "game_scenes.toml"
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func(self, context):
    self.layout.operator(GenericGameScenesExport.bl_idname)

def register():
    bpy.utils.register_class(GenericGameScenesExport)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)

def unregister():
    bpy.utils.unregister_class(GenericGameScenesExport)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)


if __name__ == "__main__":
    register()