
from settings import *

def header_byte_1gram():
    colnames = []
    for i in range(16**2):
        temp = hex(i)[2:]
        if len(str(temp))==1:
            temp = "0"+str(temp)
        colnames += ['byte_1G_'+ temp]
    return colnames


def header_byte_2grams():
    colnames = []
    colnames += ['byte_2G_'+hex(i)[2:] for i in range(16**4)]
    return colnames


def header_byte_meta_data():
    colnames = ['byte_filesize','byte_offset']
    return colnames


def header_byte_img1():
    colnames = []
    for i in range(52):
        colnames += ['byte_Img1_'+str(i)]
    return colnames


def header_byte_img2():
    colnames = []
    for i in range(108):
        colnames += ['byte_Img2_'+str(i)]
    return colnames


def header_byte_str_len():
    colnames = ['string_len_counts_' + str(x) for x in range(1,100)] + [
        'string_len_counts_0_10',
        'string_len_counts_10_30',
        'string_len_counts_30_60',
        'string_len_counts_60_90',
        'string_len_counts_0_100',
        'string_len_counts_100_150',
        'string_len_counts_150_250',
        'string_len_counts_250_400',
        'string_len_counts_400_600',
        'string_len_counts_600_900',
        'string_len_counts_900_1300',
        'string_len_counts_1300_2000',
        'string_len_counts_2000_3000',
        'string_len_counts_3000_6000',
        'string_len_counts_6000_15000',
        'string_total_len',
        'string_ratio'
    ]
    return colnames


def header_byte_entropy():
    colnames = []
    st = ['mean','var','median','max','min','max-min']

    colnames.extend( ['ent_q_diffs_' + str(x) for x in range(21) ])
    colnames.extend( ['ent_q_diffs_' + x for x in st])

    colnames.extend( ['ent_q_diff_diffs_' + str(x) for x in range(21) ])
    colnames.extend( ['ent_q_diff_diffs_' + x for x in st])

    for i in range(4):
        colnames.extend( ['ent_q_diff_block_' + str(i) + '_' + str(x) for x in range(21) ])
        colnames.extend( ['ent_q_diff_diffs_'+ str(i) + '_' + x for x in st])

    colnames.extend( ['ent_p_' + str(x) for x in range(20) ])
    colnames.extend( ['ent_p_diffs_' + str(x) for x in range(20) ])

    return colnames

######################################################################


def header_asm_meta_data():
    colnames = ['asm_md_filesize','asm_md_loc']
    return colnames


def header_asm_sym():
    symbols = ['Star','Dash','Plus','Bracket_Open','Bracket_Close','AtSign','Question', 'ExtendedAscii']
    colnames = ['asm_symb_'+reg for reg in symbols]
    return colnames


def header_asm_registers():
    registers = ['edx','esi','es','fs','ds','ss','gs','cs','ah','al',
                 'ax','bh','bl','bx','ch','cl','cx','dh','dl','dx',
                 'eax','ebp','ebx','ecx','edi','esp']

    colnames = ['asm_regs_'+reg for reg in registers]
    return colnames


def header_asm_opcodes():
    opcodes = ['add','al','bt','call','cdq','cld','cli','cmc','cmp','const','cwd','daa','db'
                ,'dd','dec','dw','endp','ends','faddp','fchs','fdiv','fdivp','fdivr','fild'
                ,'fistp','fld','fstcw','fstcwimul','fstp','fword','fxch','imul','in','inc'
                ,'ins','int','jb','je','jg','jge','jl','jmp','jnb','jno','jnz','jo','jz'
                ,'lea','loope','mov','movzx','mul','near','neg','not','or','out','outs'
                ,'pop','popf','proc','push','pushf','rcl','rcr','rdtsc','rep','ret','retn'
                ,'rol','ror','sal','sar','sbb','scas','setb','setle','setnle','setnz'
                ,'setz','shl','shld','shr','sidt','stc','std','sti','stos','sub','test'
                ,'wait','xchg','xor']

    colnames = ['asm_opcodes_'+op for op in opcodes]
    return colnames

def header_asm_opcodes2():
    opcodes = ['asm_commands_add', 'asm_commands_call', 'asm_commands_cdq', 'asm_commands_cld', 'asm_commands_cli', 'asm_commands_cmc', 'asm_commands_cmp', 'asm_commands_cwd', 'asm_commands_daa', 'asm_commands_dd', 'asm_commands_dec', 'asm_commands_dw', 'asm_commands_endp', 'asm_commands_faddp', 'asm_commands_fchs', 'asm_commands_fdiv', 'asm_commands_fdivr', 'asm_commands_fistp', 'asm_commands_fld', 'asm_commands_fstp', 'asm_commands_fword', 'asm_commands_fxch', 'asm_commands_imul', 'asm_commands_in', 'asm_commands_inc', 'asm_commands_ins', 'asm_commands_jb', 'asm_commands_je', 'asm_commands_jg', 'asm_commands_jl', 'asm_commands_jmp', 'asm_commands_jnb', 'asm_commands_jno', 'asm_commands_jo', 'asm_commands_jz', 'asm_commands_lea', 'asm_commands_mov', 'asm_commands_mul', 'asm_commands_not', 'asm_commands_or', 'asm_commands_out', 'asm_commands_outs', 'asm_commands_pop', 'asm_commands_push', 'asm_commands_rcl', 'asm_commands_rcr', 'asm_commands_rep', 'asm_commands_ret', 'asm_commands_rol', 'asm_commands_ror', 'asm_commands_sal', 'asm_commands_sar', 'asm_commands_sbb', 'asm_commands_scas', 'asm_commands_shl', 'asm_commands_shr', 'asm_commands_sidt', 'asm_commands_stc', 'asm_commands_std', 'asm_commands_sti', 'asm_commands_stos', 'asm_commands_sub', 'asm_commands_test', 'asm_commands_wait', 'asm_commands_xchg', 'asm_commands_xor']
    return opcodes

def header_asm_sections():
    kown_sections = ['.text','.data','.bss', '.rdata','.edata','.idata', '.rsrc','.tls','.reloc']
    colnames = kown_sections + ['Num_Sections', 'Unknown_Sections', 'Unknown_Sections_lines']
    colnames += ['.text_por','.data_por','.bss_por', '.rdata_por','.edata_por',
                 '.idata_por', '.rsrc_por','.tls_por','.reloc_por']
    colnames += ['known_Sections_por', 'Unknown_Sections_por', 'Unknown_Sections_lines_por']
    return colnames


def header_asm_data_define():
    colnames = ['db_por','dd_por','dw_por','dc_por','db0_por','dbN0_por','dd_text',
                'db_text','dd_rdata','db3_rdata','db3_data','db3_all','dd4','dd5',
                'dd6','dd4_all','dd5_all','dd6_all', 'db3_idata', 'db3_NdNt', 
                'db4_NdNt', 'db5_NdNt', 'db6_NdNt', 'db3_all_zero']
    return colnames


def header_asm_apis():
    defined_apis = io.read_all_lines(APIS_PATH)
    colnames = defined_apis[0].split(',')
    return colnames

def header_asm_misc():
    keywords = ['Virtual','Offset','loc','Import','Imports','var','Forwarder','UINT','LONG','BOOL','WORD','BYTES','large','short','dd','db','dw','XREF','ptr','DATA','FUNCTION','extrn','byte','word','dword','char','DWORD','stdcall','arg','locret','asc','align','WinMain','unk','cookie','off','nullsub','DllEntryPoint','System32','dll','CHUNK','BASS','HMENU','DLL','LPWSTR','void','HRESULT','HDC','LRESULT','HANDLE','HWND','LPSTR','int','HLOCAL','FARPROC','ATOM','HMODULE','WPARAM','HGLOBAL','entry','rva','COLLAPSED','config','exe','Software','CurrentVersion','__imp_','INT_PTR','UINT_PTR','---Seperator','PCCTL_CONTEXT','__IMPORT_','INTERNET_STATUS_CALLBACK','.rdata:','.data:','.text:','case','installdir','market','microsoft','policies','proc','scrollwindow','search','trap','visualc','___security_cookie','assume','callvirtualalloc','exportedentry','hardware','hkey_current_user','hkey_local_machine','sp-analysisfailed','unableto']
    keywords = ['asm_misc_'+key for key in keywords]
    return keywords