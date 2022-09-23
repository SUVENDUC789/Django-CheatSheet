from django.shortcuts import render

# Create your views here.

def home(request):
    p={
        'title':'DTL-Dynamic Template Files',
        'Creater':'Suvendu Chowdhury',
        'FrameWrok':'django',
        'langu':'python',
        'text':'Lorem ipsum dolor sit amet.(using dtl-filter)',
        'text2':'LOREM IPSUM DOLOR SIT AMET.(USING DTL-FILTER)',
        'Admin':'suvendu',
        'friends':['Supratim','Hritik','Debarpan','Bristi','Sayan'],
        'data':{
            's1':{
                'name':'suvendu',
                'roll':'s-412',
                'lang':'c,cpp,java,python,php,laravel,django,flask',
            },
            's2':{
                'name':'supratim',
                'roll':'s-411',
                'lang':'c,cpp,java,python,php,flask,django,angular,js,ts',
            },
            's3':{
                'name':'hritik',
                'roll':'s-420',
                'lang':'c',
            },
            's4':{
                'name':'debarpan',
                'roll':'s-444',
                'lang':'python,html,css,js,assembly language',
            },
            's5':{
                'name':'Sinchan',
                'roll':'s-430',
                'lang':'c,html,css,js,assembly language',
            },
            's6':{
                'name':'Ayush',
                'roll':'s-422',
                'lang':'js-framework,html,css,js',
            },
            's7':{
                'name':'sujan',
                'roll':'s-409',
                'lang':'html,assembly language',
            },
            's8':{
                'name':'ronith',
                'roll':'s-416',
                'lang':'html,assembly language,css,js',
            },
        }
    }
    return render(request,'home.html',p)
