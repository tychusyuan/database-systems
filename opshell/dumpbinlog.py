#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Dump all replication events from a remote mysql server
#
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent
import hashlib

MYSQL_SETTINGS = {
    "host": "127.0.0.1
    "port": 3306
    "user": "",
    "passwd": ""
}

def _binlog_loader(self):
    """
    read row from binlog
    """
    if self.is_binlog_sync:
        resume_stream = True
        logging.info("Resume from binlog_file: {file}  binlog_pos: {pos}".format(file=self.log_file,
                                                                                 pos=self.log_pos))
    else:
        resume_stream = False

    stream = BinLogStreamReader(connection_settings=self.binlog_conf,
                                server_id=self.config['mysql']['server_id'],
                                only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent, RotateEvent],
                                only_tables=self.tables,
                                resume_stream=resume_stream,
                                blocking=True,
                                log_file=self.log_file,
                                log_pos=self.log_pos)
    for binlogevent in stream:
        self.log_file = stream.log_file
        self.log_pos = stream.log_pos

        # RotateEvent to update binlog record when no related table changed
        if isinstance(binlogevent, RotateEvent):
            self._save_binlog_record()
            continue
        for row in binlogevent.rows:
            if isinstance(binlogevent, DeleteRowsEvent):
                if binlogevent.table == self.master:
                    rv = {
                        'action': 'delete',
                        'doc': row['values']
                    }
                else:
                    rv = {
                        'action': 'update',
                        'doc': {k: row['values'][k] if self.id_key and self.id_key == k else None for k in row['values']}
                    }
            elif isinstance(binlogevent, UpdateRowsEvent):
                rv = {
                    'action': 'update',
                    'doc': row['after_values']
                }
            elif isinstance(binlogevent, WriteRowsEvent):
                if binlogevent.table == self.master:
                    rv = {
                            'action': 'create',
                            'doc': row['values']
                        }
                else:
                    rv = {
                            'action': 'update',
                            'doc': row['values']
                        }
            else:
                logging.error('unknown action type in binlog')
                raise TypeError('unknown action type in binlog')
            yield rv
            # print(rv)
    stream.close()
    raise IOError('mysql connection closed')

def main():
    # server_id is your slave identifier, it should be unique.
    # set blocking to True if you want to block and wait for the next event at
    # the end of the stream
    stream = BinLogStreamReader(connection_settings=MYSQL_SETTINGS,
                                server_id=3,
                                blocking=True)

    for binlogevent in stream:
        print(binlogevent.event_type,binlogevent.timestamp)
        if isinstance(binlogevent, DeleteRowsEvent):
            print(hashlib.md5(bytes("".join(map(str,binlogevent.rows)),'utf-8')).hexdigest())
        elif isinstance(binlogevent, UpdateRowsEvent):
            print(hashlib.md5(bytes("".join(map(str,binlogevent.rows)),'utf-8')).hexdigest())
        elif isinstance(binlogevent, WriteRowsEvent):
            print(hashlib.md5(bytes("".join(map(str,binlogevent.rows)),'utf-8')).hexdigest())
    stream.close()


if __name__ == "__main__":
    main()
