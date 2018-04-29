# https://github.com/AlbertoRFer/Static-ESI-skill-dump
# ToDO: Use this once on program install. Add update function wich deletes old entrys, and ask for new ones (in case of new skills added by EvE)
from service.esipy import App
from service.esipy import EsiClient

import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.databaseTables import StaticSkillGroups, StaticSkills, StaticShipGroups, StaticShips, StaticModuleGroups, StaticModules

class SkillDump():
    def __init__(self, parent=None):
        super(SkillDump, self).__init__()

        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()

        app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")
        client = EsiClient(
            retry_requests=True,
            header={'User-Agent': 'DumpSkills'},
            raw_body_only=False,
        )

        fields = app.op['get_universe_categories_category_id'](
            category_id=16,
        )

        response = client.request(fields)
        groups = response.data['groups']

        gral = {}

        for group in groups:
            g = app.op['get_universe_groups_group_id'](
                group_id=group
            )
            response = client.request(g)
            group_name = response.data['name']
            group_id = response.data['group_id']
            skills = response.data['types']
            group_dict = {}

            group = StaticSkillGroups().setData(group_name, group_id)
            print(group_name)
            print(group_id)
            # print(group)

            self.session.add(group)

            for skill in skills:
                s = app.op['get_universe_types_type_id'](
                    type_id=skill
                )
                response = client.request(s)
                group_dict[skill] = response.data['name']
                skillname = response.data['name']
                skillid = response.data['type_id']

                if skillname == "Amarr Dreadnought":
                    print(response.data)

                if response.data['published'] == True:

                    skill = StaticSkills().setData(response.data)
                    self.session.add(skill)

            gral[group_name] = [{'Category ID': group}, group_dict]
            self.session.commit()

        self.session.close()
        # with open("skills.txt", 'w') as f:
        # json.dump(gral, fp=f, indent=4, sort_keys=True)

class ShipDump():
    def __init__(self, parent=None):
        super(ShipDump, self).__init__()

        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()

        app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")
        client = EsiClient(
            retry_requests=True,
            header={'User-Agent': 'DumpShips'},
            raw_body_only=False,
        )

        fields = app.op['get_universe_categories_category_id'](
            category_id=6,
        )

        response = client.request(fields)
        groups = response.data['groups']

        gral = {}

        for group in groups:
            g = app.op['get_universe_groups_group_id'](
                group_id=group
            )
            response = client.request(g)
            group_name = response.data['name']
            group_id = response.data['group_id']
            ships = response.data['types']
            group_dict = {}

            group = StaticShipGroups().setData(group_name, group_id)
            print(group_name)
            #print(group_id)
            #print(group)

            self.session.add(group)

            for ship in ships:
                s = app.op['get_universe_types_type_id'](
                    type_id=ship
                )
                response = client.request(s)
                group_dict[ship] = response.data['name']
                shipname = response.data['name']
                shipid = response.data['type_id']

                print(response.data)

                if response.data['published'] == True:
                    ship = StaticShips().setData(response.data)
                    self.session.add(ship)

            gral[group_name] = [{'Category ID': group}, group_dict]
            self.session.commit()

        # with open("skills.txt", 'w') as f:
        # json.dump(gral, fp=f, indent=4, sort_keys=True)

class ModuleDump():
    def __init__(self, parent=None):
        super(ModuleDump, self).__init__()

        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)  # once engine is available
        self.session = Session()

        app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")
        client = EsiClient(
            retry_requests=True,
            header={'User-Agent': 'DumpModules'},
            raw_body_only=False,
        )

        fields = app.op['get_universe_categories_category_id'](
            category_id=7,
        )

        response = client.request(fields)
        groups = response.data['groups']

        gral = {}

        for group in groups:
            g = app.op['get_universe_groups_group_id'](
                group_id=group
            )
            response = client.request(g)
            group_name = response.data['name']
            group_id = response.data['group_id']
            modules = response.data['types']
            group_dict = {}

            group = StaticModuleGroups().setData(group_name, group_id)
            print(group_name)
            #print(group_id)
            #print(group)

            self.session.add(group)

            for module in modules:
                s = app.op['get_universe_types_type_id'](
                    type_id=module
                )
                response = client.request(s)
                group_dict[module] = response.data['name']
                name = response.data['name']
                id = response.data['type_id']

                print(response.data)

                if response.data['published'] == True:
                    module = StaticModules().setData(response.data)
                    self.session.add(module)

            gral[group_name] = [{'Category ID': group}, group_dict]
            self.session.commit()

        # with open("skills.txt", 'w') as f:
        # json.dump(gral, fp=f, indent=4, sort_keys=True)


if __name__ == "__main__":

   SkillDump()
   ShipDump()
   ModuleDump()
