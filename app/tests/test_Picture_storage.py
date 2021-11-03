import model
import time

model.commands.connection.Connection().initialize_g81_dmc()
model.commands.registration.Registration().execute()
model.picturecontrol.storage_controller.Storage_controller().download_index()


time.sleep(10)
model.picturecontrol.storage_controller.Storage_controller().download_all("./aaa/","original")
