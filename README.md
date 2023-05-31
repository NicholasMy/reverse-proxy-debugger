# Reverse Proxy Debugger
A web application that shows the raw request it receives to help debug reverse proxy issues

## Usage
1. Choose the host port in docker-compose.yml (default is 5050)
2. Run `docker compose up -d`
3. Point your reverse proxy to the port you chose
4. Connect to your reverse proxy and see the request details

## Supports
- Method
- Path
- Query parameters
- Headers
- Body (JSON, form data, and raw)
- Source IP and port

## Output
The request details are displayed in the browser AND logged to stdout.
Use `docker compose logs -f` to view the live output.

## Screenshots

![image](https://github.com/NicholasMy/reverse-proxy-debugger/assets/32116122/be97ea3e-b793-452c-8daf-5d1aa42b27df)

![image](https://github.com/NicholasMy/reverse-proxy-debugger/assets/32116122/31593594-9ce4-4ee1-ae24-272e9012d887)

![image](https://github.com/NicholasMy/reverse-proxy-debugger/assets/32116122/f67abee8-342b-47f2-be5a-342118863f1b)
