// 修改后的安全版本
<script>
(function(){
    if(!window.chatbase || window.chatbase("getState") !== "initialized"){
        window.chatbase = (...arguments) => {
            if(!window.chatbase.q){
                window.chatbase.q = [];
            }
            window.chatbase.q.push(arguments);
        };
        window.chatbase = new Proxy(window.chatbase, {
            get(target, prop){
                if(prop === "q"){
                    return target.q;
                }
                return (...args) => target(prop, ...args);
            }
        });
    }
    
    const onLoad = function(){
        const script = document.createElement("script");
        script.src = "https://www.chatbase.co/embed.min.js";
        script.id = "06_63h9wgHu7IeP5wxk1m"; // 你的实际 ID
        script.domain = "www.chatbase.co";
        script.defer = true; // 添加 defer 属性
        document.body.appendChild(script);
    };
    
    if(document.readyState === "complete"){
        onLoad();
    } else {
        window.addEventListener("load", onLoad);
    }
})();
</script>
