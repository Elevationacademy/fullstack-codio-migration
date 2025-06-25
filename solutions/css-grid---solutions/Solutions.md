
Chat UI Exercise
--
html:
```html
<div id="container">
	

	        <div id="contact-container">
	            <div id="contact-head">Friends</div>
	            <div class="friend">Freya</div>
	            <div class="friend">Linda</div>
	            <div class="friend">Kenan</div>
	            <div class="friend">Theresa</div>
	        </div>
	

	        <div id="chat-container">
	            <div id="message-container">
	                <div class="message friend-message">
	                    <div class="message-text">Hey</div>
	                    <div class="message-time">14:00</div>
	                </div>
	                <div class="message friend-message">
	                    <div class="message-text">Hello?</div>
	                    <div class="message-time">14:31</div>
	                </div>
	                <div class="message my-message">
	                    <div class="message-text">Sorry, been busy</div>
	                    <div class="message-time">17:58</div>
	                </div>
	                <div class="message friend-message">
	                    <div class="message-text">You work too much</div>
	                    <div class="message-time">17:59</div>
	                </div>
	                <div class="message my-message">
	                    <div class="message-text">Tell me about it</div>
	                    <div class="message-time">17:59</div>
	                </div>
	            </div>
	            <div id="editor-container">
	                <input id="write-message" type="text" placeholder="Type a message">
	                <div id="send-button" onclick="sendMessage()">SEND</div>
	            </div>
	        </div>
	

	    </div>
	

	    </div>
```
  
CSS:

  
```css
#container {
	    display: grid;
	    height: 100vh;
	    grid-template-columns: 1fr 4fr;
	

	}
	

	#contact-container {
	    display: grid;
	    background-color: #8E44AD;
	    height: 100%;  
	    padding-right: 10px;
	    padding-left: 10px;
	    font-family: 'Inconsolata', monospace;
	

	}
	

	#contact-head {
	    font-weight: bold;
	    margin-left: 8px;
	    margin-top: 10px;
	}
	

	.friend {
	    background-color: #9B59B6;
	    height: 5vh;
	    border-radius: 3px;
	    align-content: center;
	    display: grid;
	    padding-left: 5px;
	}
	

	#chat-container {
	    display: grid;
	    grid-template-rows: 9fr 1fr;
	    background-color: #ECF0F1;
	}
	

	#message-container {
	    display: grid;
	    grid-template-rows: repeat(5, 1fr);
	    grid-gap: 60px;
	}
	

	

	.message {
	    
	    display: grid;
	    grid-template-areas: 
	    "m t";
	

	    border-radius: 7px;
	    margin-left: 10px;
	    margin-right: 10px;
	    grid-gap: 20px;
	

	    margin-bottom: 10px;
	    margin-top: 10px;
	    
	}
	

	.friend-message {
	    display: grid;
	    justify-self: start;
	    background-color: #2ecc71;
	}
	

	.my-message {
	    display: grid;
	    justify-self: end;
	    background-color: #BDC3C7;
	}
	

	.message-text {
	    font-family: 'Indie Flower', cursive;
	    display: grid;
	    grid-area: m;
	    padding-left: 8px;
	    align-self: center;
	    justify-self: start;
	}
	

	.message-time {
	    font-family: 'Gloria Hallelujah', cursive;
	    display: grid;
	    grid-area: t;
	    padding-right: 8px;
	    padding-bottom: 3px;
	    justify-self: end;
	    align-self: end;
	    font-size: 12px;
	}
	

	

	#editor-container {
	    
	    display: grid;
	    grid-template-columns: 4fr 1fr;
	    height: 100%;
	}
	

	#write-message {
	

	    font-size: 12px;
	    display: grid;
	    padding-left: 5px;
	    border: grey solid 1px;
	    align-content: center;
	    background-color: #FFFFFF;
	}
	

	#send-button{
	    font-size: 14px;
	    display: grid;
	    align-content: center;
	    justify-content: center;
	    background-color: #8E44AD;
	}
```

