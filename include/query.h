#ifndef QUERY_H
#define QUERY_H

#include <mysql/mysql.h>

// Variables globales para conectarse a MySQL
#define MYSQL_HOST "localhost"
#define MYSQL_USER "root"

// Base de datos historicos y publicos
#define DB "MatchaFundingMySQL"

char *EjecutarQueryEnJSON(const char *query);
char *ParsearResultadoEnJSON(MYSQL_RES *result);

#endif
