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
![Screenshot from 2023-05-31 10-51-33](https://github.com/NicholasMy/reverse-proxy-debugger/assets/32116122/226df83c-2766-4f33-b397-2af2368babff)

![Screenshot from 2023-05-31 10-54-09](https://github.com/NicholasMy/reverse-proxy-debugger/assets/32116122/08446f0c-103a-4743-b712-1917674ab4ec)

![Screenshot from 2023-05-31 10-58-18](https://github.com/NicholasMy/reverse-proxy-debugger/assets/32116122/bc98d6d3-1abb-47d9-b55a-f73936f7dffd)
