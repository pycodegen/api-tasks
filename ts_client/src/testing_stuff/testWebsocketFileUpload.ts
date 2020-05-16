import {
  connect,
} from 'socket.io-client'

import * as fs from 'fs';
import * as Blob from 'cross-blob';



// 일단은: file-chunking 은 나중에?
// BaseRemoteFilesReceiver
//   - BaseChunkFilesReceiver
function connectSocketIO(args: {
  url: string,
  opts?: SocketIOClient.ConnectOpts,
}) {
  return new Promise<SocketIOClient.Socket>((resolve, reject) => {
    const connection = connect(args.url, args.opts);
    connection.once('connect', () => resolve(connection))
  })
}

async function uploadFile(file: File, sliceSize) {
  file.slice()
}

async function main() {
  // const connection = connect('localhost:30001');
  // const file = await fs.read('')
  const socket = await connectSocketIO({
    url: 'http://localhost:30001',
  })
  const data = new Uint8Array([
    1,2,3,5,6,7,8,9,1,2,3,5,6,7,8,9,1,2,3,5,6,7,8,9,1,2,3,5,6,7,8,9,
  ]);
  const binData = data.buffer;
  const blob = new Blob(['0132-23423-23434*', binData])
  const arrayBuffer = await blob.arrayBuffer()
  const dv = new DataView(arrayBuffer, 0, 20)
  socket.emit('file_upload', dv.buffer)
  console.error('1')
  socket.close()
}

main()