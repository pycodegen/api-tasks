import SHA256 from 'jssha/dist/sha256'
import range from 'ramda/es/range'
// import {
//   SocketIOClient,
// } from 'socket.io-client'
import {
  Socket,
} from 'socket.io-client'
import { BaseRemoteFileSender } from "./BaseRemoteFileSender";
// import * as sha256 from 'crypto-js/sha256';
// import * as encLatin1 from 'crypto-js/enc-latin1'

export type FileMeta = {
  chunkSizeInBytes: number;
  chunkHashes: string[];
}

export type RegisteredFileToSend = {
  fileAsArrayBuffer: ArrayBuffer,
  meta: FileMeta,
}

export type FileToSendId = string & {
  __fileToSendId: null,
}

export class SocketIORemoteFileSender extends BaseRemoteFileSender {
  constructor(
    public socketioClient: SocketIOClient.Socket,
  ) {
    super();
  }

  registeredFilesToSend: Map<FileToSendId, RegisteredFileToSend> = new Map()
  async registerFileToSend({
    fileAsArrayBuffer,
    taskId,
    paramName,
    timeout,
  }: {
    fileAsArrayBuffer: ArrayBuffer,
    taskId: string,
    paramName: string,
    timeout?: number,
  }) {
    // 1. break into chunks, get hashsums
    const fileMeta = await this.getFileMetadata({
      fileAsArrayBuffer,
      paramName,
      taskId
    })

  }
  async getFileMetadata(args: {
    fileAsArrayBuffer: ArrayBuffer,
    taskId: string,
    paramName: string,
    timeout?: number,
    chunkSizeInBytes?: number,
  }): Promise<FileMeta> {
    const chunkSizeInBytes = args.chunkSizeInBytes || 1000000;
    const numChunks = Math.ceil(args.fileAsArrayBuffer.byteLength / chunkSizeInBytes)
    const chunkHashes = range(0, numChunks)
      .map(index => {
        const fileSlice = args.fileAsArrayBuffer.slice(
          index * numChunks,
          (index + 1) * numChunks,
        )
        const sha256 = new SHA256('SHA-256', 'ARRAYBUFFER')
        sha256.update(fileSlice)
        return sha256.getHash('B64')
      })
    return {
      chunkSizeInBytes,
      chunkHashes,
    }
  }
  async sendFileChunk(args: {
    fileToSendId: FileToSendId,
    nthChunk: number,
  }) {
    const registeredFileToSend = this.registeredFilesToSend.get(args.fileToSendId);
    const chunkSizeInBytes = registeredFileToSend.meta.chunkSizeInBytes
    const fileSlice = registeredFileToSend
      .fileAsArrayBuffer.slice(
        args.nthChunk * chunkSizeInBytes,
        (args.nthChunk + 1) * chunkSizeInBytes,
      )
    this.
  }
}