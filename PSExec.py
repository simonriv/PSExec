import json_manager
import click

@click.group()
def PSExec():
    pass

@PSExec.command()
@click.option('--name','-n',required=True,help='Name of the script')
@click.option('--desc','-d',required=True,help='Description of the script')
@click.option('--path','-p',required=True,help='Path of the script')
@click.option('--module','-m',required=True,help='Module of the script')
@click.option('--tags','-t',required=True,multiple=True,help='Tags of the script')
@click.pass_context
def new(ctx,name,desc,path,module,tags):
    if not name or not desc or not path or not module or not tags:
        ctx.fail('The all fields are required.')
    else:
        data = json_manager.read_json()
        newId = len(data) + 1
        
        folder = json_manager.create_folder('./scripts')

        if not folder:
            print(f"The folder scripts already exists.")
        
        moveScript = json_manager.move_file(path,'./scripts')
        
        if not moveScript:
            ctx.fail('Could not be moved the file to the folder scripts.')

        newScript = {
            'id': newId,
            'name': name,
            'description': desc,
            'path': moveScript,
            'module': module,
            'tags': tags,
        }
        data.append(newScript)
        json_manager.write_json(data)
        print(f"The Script - {name} created successfully with id {newId}")

@PSExec.command()
def scripts():
    data = json_manager.read_json()

    if len(data) == 0:
        print("Don't exist scripts, please add scripts for use.")
    else:
        print("NAME".ljust(20),"DESC".ljust(len(data[0]['description'])),"MODULE".ljust(20), "TAGS".ljust(20))
        for script in data:
            tagg = ''
            for tag in script['tags']:
                tagg += '[' + tag + ']'

            print(script['name'].ljust(20),script['description'].ljust(20),script['module'].ljust(20),tagg.ljust(20))

@PSExec.command()
@click.option('--name','-n',required=True,help='Name of the script')
@click.pass_context
def exec(ctx,name):
    execFile = json_manager.exec_file(name)
    if execFile == 0:
        print(f"The {name} script has been executed successfully.")
    else:
        print(f"The {name} script has not been executed correctly.")


if __name__ == '__main__':
    PSExec()
