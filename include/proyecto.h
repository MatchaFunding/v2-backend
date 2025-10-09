#ifndef PROYECTO_H
#define PROYECTO_H

#include "utils.h"

char* VerTodosLosProyectos(const char *url);
enum MHD_Result URLProyecto
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
