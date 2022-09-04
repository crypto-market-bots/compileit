import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {
 code : any  ;
  constructor() { }

  ngOnInit(): void {
  }
 
  data(code : NgForm){
  console.log(code.value.editor);
  this.code = code.value.editor;
  let res = JSON.stringify(code.value.data);
  console.log(res);
  }
  
}
