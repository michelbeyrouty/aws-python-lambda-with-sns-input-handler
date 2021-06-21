from app.controllers import test

routes = {
    "TEST": test
}


def fetch_controller(snsTopic):
    controller = routes.get(snsTopic, "notFound")
    if controller == "notFound":
        raise TypeError("Controller not found")

    return controller
