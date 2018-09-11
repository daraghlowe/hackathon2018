import digitalocean

apikey="key_woz_ere"
manager = digitalocean.Manager(token=apikey)

hostname = "web4"
region_id = "lon1"
image_id = "37208325"
droplet_size = "s-1vcpu-1gb"
tag_list = ["web"]


def create_droplet(token, name, region, image, size, tags):
    droplet = digitalocean.Droplet(token=token,
                                   name=name,
                                   region=region,
                                   image=image,
                                   size_slug=size,
                                   backups=False,
                                   tags=tags)
    droplet.create()


def get_last_node(tag_name):
    node_list = manager.get_all_droplets(tag_name=tag_name)
    last_node = node_list[-1].name
    return last_node


def get_next_node(tag_name):
    last_node = get_last_node(tag_name)
    last_node_num = int(last_node.split("-")[-1])
    next_node_num = last_node_num + 1
    next_node = '{}{}'.format('web-', format(next_node_num, '02d'))
    return next_node
