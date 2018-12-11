import { NavController, NavParams } from 'ionic-angular';
import { Component } from '@angular/core';

@Component({
    selector: 'page-login',
    templateUrl: 'login.html'
})

export class LoginPage {
    
    email: string;
    password: string;

    constructor(
        public navCtrl: NavController,
        public navParams: NavParams,
    ) {
        
    }
}