<script lang="ts">
    import imgUrl from "../assets/sample-cat.jpg"
import cv from "opencv-ts"
    
    
    /* import {    
        ArrayQueue,
        ConstantBackoff,
        Websocket,
        WebsocketBuilder,
        WebsocketEvent,
    } from "websocket-ts";
    
    const ws = new WebsocketBuilder("ws://192.168.1.62:8888")
    .withBuffer(new ArrayQueue())
    .withBackoff(new ConstantBackoff(1000))
    .build();

    const printMessage = (i: Websocket, ev: MessageEvent) => {
        console.log(`received message: ${ev.data}`);
    }

    ws.addEventListener(WebsocketEvent.open, () => console.log("opened!"));
    ws.addEventListener(WebsocketEvent.close, () => console.log("closed!"));
    ws.addEventListener(WebsocketEvent.message, printMessage); */

</script>

<div>
    <img src={imgUrl} alt="a cat looking into a camera" width=640 height=480>
    <!-- svelte-ignore a11y_media_has_caption -->
    <video width="640" height="480">
        <source src="http://192.168.1.62:5000">
    </video>
    
</div>