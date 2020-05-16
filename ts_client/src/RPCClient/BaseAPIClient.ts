export type TaskArgs<
  ArgsDict,
  FuncName extends string = string,
> = {
  funcName: string;
  argsDict: ArgsDict
}

export abstract class BaseRPCClient {
  extractFileParams(argsDict: { [key: string]: any }) {

  }
  send(args: TaskArgs<any>) {

  }
}