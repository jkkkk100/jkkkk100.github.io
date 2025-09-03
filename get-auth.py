<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbase认证修复方案</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
            color: #f0f6fc;
            line-height: 1.6;
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(13, 17, 23, 0.8);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        header {
            background: #0d1117;
            color: #f0f6fc;
            padding: 30px;
            text-align: center;
            border-bottom: 1px solid #21262d;
        }
        
        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: #58a6ff;
        }
        
        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .content {
            display: flex;
            flex-wrap: wrap;
            padding: 20px;
        }
        
        .problem, .solution {
            flex: 1;
            min-width: 300px;
            padding: 20px;
        }
        
        .problem {
            border-right: 1px solid #21262d;
        }
        
        .card {
            background: #161b22;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 25px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            border: 1px solid #30363d;
        }
        
        .card h3 {
            color: #58a6ff;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }
        
        .card h3 i {
            margin-right: 10px;
        }
        
        .code {
            background: #0d1117;
            color: #c9d1d9;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            overflow-x: auto;
            font-family: 'Fira Code', monospace;
            border: 1px solid #30363d;
        }
        
        .error {
            color: #f85149;
            background: rgba(248, 81, 73, 0.1);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            border-left: 4px solid #f85149;
        }
        
        .success {
            color: #3fb950;
            background: rgba(63, 185, 80, 0.1);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            border-left: 4px solid #3fb950;
        }
        
        .btn {
            display: inline-block;
            background: #238636;
            color: white;
            padding: 12px 25px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
            margin: 10px 0;
            transition: background 0.2s;
            border: none;
            cursor: pointer;
        }
        
        .btn:hover {
            background: #2ea043;
        }
        
        .test-area {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: #161b22;
            border-radius: 10px;
            border: 1px solid #30363d;
        }
        
        @media (max-width: 768px) {
            .content {
                flex-direction: column;
            }
            .problem {
                border-right: none;
                border-bottom: 1px solid #21262d;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fas fa-bug"></i> Chatbase认证API修复方案</h1>
            <p>解决get-auth.py中的500内部服务器错误</p>
        </header>
        
        <div class="content">
            <div class="problem">
                <div class="card">
                    <h3><i class="fas fa-exclamation-triangle"></i> 问题分析</h3>
                    <p>您的<code>get-auth.py</code>文件返回了500内部服务器错误，代码：<code>FUNCTION_INVOCATION_FAILED</code>。</p>
                    
                    <div class="error">
                        <p><strong>错误详情：</strong> ID: sin1::h948p-1756880933757-c0a86b0c4b31</p>
                        <p>这通常表示函数调用失败，可能是由于以下原因：</p>
                        <ul>
                            <li>缺少必要的依赖项</li>
                            <li>代码语法错误</li>
                            <li>导入模块失败</li>
                            <li>函数签名不正确</li>
                        </ul>
                    </div>
                </div>
                
                <div class="card">
                    <h3><i class="fas fa-file-code"></i> 原始代码</h3>
                    <div class="code">
# api/get-auth.py<br>
import hmac, hashlib, time, random<br>
from flask import Request<br>
<br>
SECRET = "rhkigrqj0ci7ora0a1iuoz602qjm07d7"  # 你的 Chatbase 密钥<br>
<br>
def handler(request: Request):<br>
&nbsp;&nbsp;&nbsp;&nbsp;# 随机生成 userId<br>
&nbsp;&nbsp;&nbsp;&nbsp;user_id = f"guest_{int(time.time())}_{random.randint(1000,9999)}"<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;# 生成 authToken<br>
&nbsp;&nbsp;&nbsp;&nbsp;auth_token = hmac.new(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SECRET.encode(), user_id.encode(), hashlib.sha256<br>
&nbsp;&nbsp;&nbsp;&nbsp;).hexdigest()<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;return {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"userId": user_id,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"authToken": auth_token<br>
&nbsp;&nbsp;&nbsp;&nbsp;}
                    </div>
                </div>
            </div>
            
            <div class="solution">
                <div class="card">
                    <h3><i class="fas fa-wrench"></i> 修复方案</h3>
                    <p>以下是修复后的代码，解决了可能的问题：</p>
                    
                    <div class="code">
# api/get-auth.py<br>
import hmac<br>
import hashlib<br>
import time<br>
import random<br>
from flask import jsonify<br>
<br>
SECRET = "rhkigrqj0ci7ora0a1iuoz602qjm07d7"  # 你的 Chatbase 密钥<br>
<br>
def handler(request):<br>
&nbsp;&nbsp;&nbsp;&nbsp;try:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 随机生成 userId<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_id = f"guest_{int(time.time())}_{random.randint(1000,9999)}"<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 生成 authToken<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_token = hmac.new(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SECRET.encode(), <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_id.encode(), <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashlib.sha256<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;).hexdigest()<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return jsonify({<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"userId": user_id,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"authToken": auth_token<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;})<br>
&nbsp;&nbsp;&nbsp;&nbsp;except Exception as e:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return jsonify({"error": str(e)}), 500
                    </div>
                    
                    <div class="success">
                        <p><strong>主要改进：</strong></p>
                        <ul>
                            <li>添加了异常处理，提供更好的错误信息</li>
                            <li>使用<code>jsonify</code>确保正确的JSON响应</li>
                            <li>简化了函数签名，移除类型注解以避免导入问题</li>
                            <li>改进了代码格式，提高可读性</li>
                        </ul>
                    </div>
                </div>
                
                <div class="test-area">
                    <h3><i class="fas fa-vial"></i> 测试修复</h3>
                    <p>点击下方按钮测试认证API是否正常工作：</p>
                    <button class="btn" onclick="testAuth()">测试认证API</button>
                    <div id="test-result"></div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"></script>
    <script>
        async function testAuth() {
            const resultDiv = document.getElementById('test-result');
            resultDiv.innerHTML = '<p>正在测试API...</p>';
            
            try {
                // 这里应该替换为您的API端点
                const response = await fetch('/api/get-auth');
                const data = await response.json();
                
                if (data.userId && data.authToken) {
                    resultDiv.innerHTML = `
                        <div class="success">
                            <p><strong>测试成功！</strong></p>
                            <p>用户ID: ${data.userId}</p>
                            <p>认证令牌: ${data.authToken.substring(0, 20)}...</p>
                        </div>
                    `;
                } else {
                    resultDiv.innerHTML = `
                        <div class="error">
                            <p><strong>API返回了意外结果：</strong></p>
                            <pre>${JSON.stringify(data, null, 2)}</pre>
                        </div>
                    `;
                }
            } catch (error) {
                resultDiv.innerHTML = `
                    <div class="error">
                        <p><strong>测试失败：</strong> ${error.message}</p>
                        <p>请检查您的API端点是否正确部署。</p>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>

