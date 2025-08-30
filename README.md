# TheBigBadWall

Simple Flask firewall to block all unwanted GET requests and allow only your Lua endpoint and root.

## Deployment

1. Push this repo to GitHub.
2. Create a Render Web Service.
3. Choose **Python/Flask** environment (niet Docker nodig).
4. Render zal automatisch dependencies installeren van requirements.txt en `firewall.py` draaien.
5. Firewall draait op poort 80, blokkeert alle andere requests dan `/` en de Lua endpoint.
