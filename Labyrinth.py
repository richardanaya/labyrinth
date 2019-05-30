bl_info = {
    "name": "Labyrinth",
    "category": "Import-Export",
}

import bpy
import os

def write_generic_game_scene(collection,filePath):
    scene_file = open(filePath, "w")
    scene_file.write("name=\"{0}\"\n".format(collection.name))
    for o in collection.objects:
        scene_file.write("[{0}]\n".format(o.name))
        scene_file.write("position=[{0},{1},{2}]\n".format(o.position.x,o.position.y,o.position.z))
    scene_file.close()
    

def write_generic_game_scenes(filePath):
    target_dir = os.path.dirname(filePath)
    print(dir)
    scenes_file = open(filePath, "w")
    scenes_file.write("version=1\n")
    for c in bpy.data.collections:
        scenes_file.write("[{0}]\n".format(c.name))
        scene_file = "scene_"+c.name.replace(" ","_")+".toml"
        scenes_file.write("file=\"{0}\"\n".format(scene_file))
        write_generic_game_scene(c,os.path.join(target_dir,scene_file))
    scenes_file.close()

class GenericGameScenesExport(bpy.types.Operator):
    """Export Generic Game Scenes"""
    bl_idname = "object.export_generic_game_scenes"
    bl_label = "Generic Game Scenes (.toml)"
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