# -*- coding: utf-8 -*-

def on_user_info(server, info):
	if server.get_permission_level(info) > 0:
		if info.content == '!!restart':
			server.restart()

def on_load(server, old):
	server.add_help_message('!!restart', '重启服务器')
