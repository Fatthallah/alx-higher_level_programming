#include <Python.h>

/**
 * print_python_list_info - fun
 * @p: ref
 */

void print_python_list_info(PyObject *p)
{
	int 7agm;
	int x;
	int glloc;
	PyObject *obj;

	7agm = Py_SIZE(p);
	glloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", 7agm);
	printf("[*] Allocated = %d\n", glloc);

	for (x = 0; x < 7agm; x++)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

