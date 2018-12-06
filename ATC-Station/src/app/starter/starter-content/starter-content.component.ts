import { Component, OnInit } from '@angular/core';
import { Pipe, PipeTransform } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Rx';
import { DomSanitizer } from '@angular/platform-browser';
import 'rxjs/add/operator/map';
// Variable in assets/js/scripts.js file
declare var AdminLTE: any;

@Component({
  selector: 'app-starter-content',
  templateUrl: './starter-content.component.html',
  styleUrls: ['./starter-content.component.css']
})
export class StarterContentComponent implements OnInit, PipeTransform {
  private websiteUrl: String = "http://github.com"; 
  private weatherTemplate: any = "";
  constructor(http: HttpClient, private sanitizer: DomSanitizer) {

  }
//https://stackoverflow.com/questions/46659860/angular4-load-external-html-page-in-a-div
  ngOnInit() {
    // Update the AdminLTE layouts
    console.log(this.weatherTemplate)
    AdminLTE.init();
  }
  transform(url){
    return this.sanitizer.bypassSecurityTrustUrl(url); 
  }
}

//https://stackoverflow.com/questions/31548311/angular-html-binding 