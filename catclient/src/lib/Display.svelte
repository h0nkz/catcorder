<script lang="ts">
    import imgUrl from "../assets/sample-cat.jpg"
    import { pingServer } from "../testsocket"
</script>

<div>
    <img src={imgUrl} alt="a cat looking into a camera" width=640 height=480>
    <button onclick={pingServer}>Ping server</button>
</div>