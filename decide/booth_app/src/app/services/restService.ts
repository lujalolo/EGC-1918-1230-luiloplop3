import { HttpClient } from '@angular/common/http';
import { ConfigService } from './../../config/configService';
import { AbstractService } from './abstractService';
import { Injectable } from "@angular/core";


@Injectable()
export class RestService extends AbstractService {
    path: string;

    constructor(
        private config: ConfigService,
        http: HttpClient
    ) {
        super(http);
        //Localhost:8080
        this.path = this.config.getConfig().restUrlPrefix;
    }

    //Methods
    public logout(): Promise<any> {
        return this.makeGetRequest(this.path + 'logout', null).then((res) => {
            return Promise.resolve(res);
        }).catch((error) => {
            return Promise.reject(error);
        }); 
    }

}