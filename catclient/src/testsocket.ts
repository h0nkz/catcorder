import {
  ArrayQueue,
  ConstantBackoff,
  Websocket,
  WebsocketBuilder,
  WebsocketEvent,
} from "websocket-ts";





export function pingServer() {
    const ws = new WebsocketBuilder("ws://192.168.1.62:8888")
    .withBuffer(new ArrayQueue())
    .withBackoff(new ConstantBackoff(1000))
    .build();

}
