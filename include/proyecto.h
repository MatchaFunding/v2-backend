#ifndef PROYECTO_H
#define PROYECTO_H

#include "utils.h"

char* VerTodosLosProyectos(const char *url);
char* VerSoloUnProyecto(const char *id);
enum MHD_Result URLProyecto
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
