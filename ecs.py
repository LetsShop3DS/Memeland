from core import app
#eShop's ECS (ECommerceSOAP) server. Handles all sorts of things.
@app.route("/ecs")
def ecs():
    return "<p>konichiwa we are ecs</p>"