export abstract class BaseRemoteFileSender {

  abstract registerFileToSend(args: {
    file: File,
    taskId: string,
    paramName: string,
    timeout?: number,
  }): Promise<void>
}