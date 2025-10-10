#ifndef SEXO_H
#define SEXO_H

#include "utils.h"

char* VerSexos(const char *url);
enum MHD_Result URLSexo
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
