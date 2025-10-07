#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql/mysql.h>
#include "../include/query.h"

/* Funcion que escapa todas las comillas dobles en un string */
char *EscaparComillas(const char *input) {
	if (!input) 
		return NULL;
	size_t len = strlen(input);
	size_t extra = 0;
	for (size_t i = 0; i < len; i++) {
		if (input[i] == '"')
			extra++;
	}
	char *result = malloc(len + extra + 1);
	size_t j = 0;
	for (size_t i = 0; i < len; i++) {
		if (input[i] == '"') {
		    result[j++] = '\\';
		    result[j++] = '"';
		} 
		else {
			result[j++] = input[i];
		}
	}
	result[j] = '\0';
	return result;
}

/* Realiza la query en MySQL y devuelve la respuesta en JSON */
char *EjecutarQueryEnJSON(const char *query) {
	MYSQL *con = mysql_init(NULL);
	if (con == NULL) {
		fprintf(stderr, "Couldn't initialize database\n");
		return NULL;
	}
	if (mysql_real_connect(con, MYSQL_HOST, MYSQL_USER, NULL, DB, 0, NULL, 0) == NULL) {
		fprintf(stderr, "Couldn't connect to database\n");
		return NULL;
	}
	if (mysql_query(con, query)) {
		fprintf(stderr, "Invalid query or parameters\n");
		return NULL;
	}
	MYSQL_RES *result = mysql_store_result(con);
	if (result == NULL) {
		fprintf(stderr, "No results from query\n");
		return NULL;
	}
	char *json = ParsearResultadoEnJSON(result);
	mysql_free_result(result);
	mysql_close(con);
	return json;
}

/* Toma la respuesta de MySQL y la transforma en un arreglo JSON */
char *ParsearResultadoEnJSON(MYSQL_RES *result) {
	int num_fields = mysql_num_fields(result);
	int num_rows = mysql_num_rows(result);
	int curr_row = 0;
	int total_size = num_rows * (2 + num_fields * 256) + num_rows - 1 + 3;
	char *json = (char *)malloc(total_size);
	json[0] = '\0';
	if (num_rows == 0) {
		strcat(json, "[]");
		return json;
	}
	MYSQL_ROW row;
	strcat(json, "[");
	while ((row = mysql_fetch_row(result))) {
		strcat(json, "{");
		for(int i = 0; i < num_fields; i++) {
			MYSQL_FIELD *field = mysql_fetch_field_direct(result, i);
			strcat(json, "\"");
			strncat(json, field->name, total_size - strlen(json) - 5);
			strcat(json, "\":");
			if (IS_NUM(field->type)) // Si es un numero, no incluye las comillas dobles
				strncat(json, row[i] ? row[i] : "NULL", total_size - strlen(json) - 5);
			else {
				strcat(json, "\"");
				char *my_row = EscaparComillas(row[i]); // Se escapan las comillas
				strncat(json, my_row ? my_row : "NULL", total_size - strlen(json) - 5);
				strcat(json, "\"");
			}
			if (i < num_fields - 1)
				strcat(json, ",");
		}
		strcat(json, "}");
		if (curr_row < num_rows - 1)
			strcat(json, ",");
		curr_row++;
	}
	strcat(json, "]");
	return json;
}
