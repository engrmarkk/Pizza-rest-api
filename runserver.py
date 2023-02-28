from pizza import create_app
from pizza.config import config_dict

app = create_app(config=config_dict['prod'])

if __name__=="__main__":
    app.run(debug=True)
