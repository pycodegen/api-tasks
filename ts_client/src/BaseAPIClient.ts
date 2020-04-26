export type TaskArgs<
  ArgsDict,
  FuncName extends string = string,
> = {
  funcName: string;
  argsDict: ArgsDict
}

export abstract class BaseAPIClient {
  send(args: TaskArgs<any>) {

  }
}