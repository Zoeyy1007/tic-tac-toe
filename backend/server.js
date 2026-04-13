const {spawn} = require('child_process');

app.post('/get-ai-move', (req,res)=>{
    const boardState = JSON.stringify(req.body.squares);

    // spawn the python process
    const pythonProcess = spawn('python3', ['ai/api_bridge.py', boardState]);

    pythonProcess.stdout.on('data', (data)=>{
        res.json({move: parseInt(data.toString())})
    });
});