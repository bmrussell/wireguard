# Home VPN Wireguard setup in Docker

## References
- Container details at [Linuxserver.io](https://docs.linuxserver.io/images/docker-wireguard)
- [Christian Lempa Guide](https://www.youtube.com/watch?v=GZRTnP4lyuo)
- [Monitoring](https://www.procustodibus.com/blog/2021/01/how-to-monitor-wireguard-activity/)

## Additional
Get connection logs in JSON format with:

```bash
docker exec -it wireguard wg show all dump | ./conv.py
```