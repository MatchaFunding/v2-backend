#ifndef QUERY_H
#define QUERY_H

#include <mysql/mysql.h>

// Variables globales para conectarse a MySQL
#define MYSQL_HOST "localhost"
#define MYSQL_USER "root"

// Base de datos historicos y publicos
#define DB "MatchaFundingMySQL"

// Base de datos privados de los usuarios
#define USER_DB "MatchaDrinkersMySQL"

char *EjecutarQueryEnJSON(const char *query, const char *db);
char *ParsearResultadoEnJSON(MYSQL_RES *result);

#endif
