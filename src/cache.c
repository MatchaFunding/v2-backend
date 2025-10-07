#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <hiredis/hiredis.h>
#include "../include/cache.h"

/*
Se utiliza Redis como diccionario de cache en memoria para poder
acceder rapidamente a valores ya computados y formateados en las
vistas.
*/

/* Se intenta conectar con el diccionario de cache en memoria */
redisContext *ConexionCache() {
	redisContext *conn = redisConnect(CACHE_HOST, CACHE_PORT);
	if (conn->err) {
		printf("error: %s\n", conn->errstr);
		return NULL;
	}
	return conn;
}

/* Buscar un valor en el diccionario de cache en memoria */
char* BuscarEnCache(const char *key) {
	char *res = NULL;
	redisContext *conn = ConexionCache();
	if (conn) {
		redisReply *reply = redisCommand(conn, "GET %s", key);
		if (reply->str) {
			size_t len = strlen(reply->str);
			res = malloc(sizeof(char)*len);
			strcpy(res, reply->str);
		}
		freeReplyObject(reply);
		redisFree(conn);
	}
	return res;
}

/* Guarda un valor en el diccionario de cache en memoria */
void GuardarEnCache(const char *key, const char *value) {
	redisContext *conn = ConexionCache();
	if (conn) {
		redisReply *reply = redisCommand(conn, "SET %s %s", key, value);
		freeReplyObject(reply);
		redisFree(conn);
	}
}
